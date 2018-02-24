"use strict";

const fs = require('fs');
const path=require('path');
const ejs = require('ejs');

const pagesDirectory=path.join(__dirname, "pages");
const docsDirectory=path.join(__dirname,"..","docs");

function compileFile(inputFile, outDir){
    const filename = path.parse(inputFile).name;
    console.log("-",filename);
    const template = fs.readFileSync(inputFile, 'utf-8');
    const html = ejs.render(template, {filename: inputFile});
    fs.writeFileSync(path.join(outDir,filename+".html"), html);
}

function getFiles(baseDir){
    return fs.readdirSync(baseDir).map((f)=>path.join(baseDir,f));
}

function clearDirectoryFromHtml(dir){
    const pages=getFiles(dir);
    for(const page of pages){
        if(path.extname(page)===".html"){
            fs.unlinkSync(page)
        }
    }
}


// ------------

clearDirectoryFromHtml(docsDirectory)
const pages = getFiles(pagesDirectory);

for(const file of pages){
    compileFile(file, docsDirectory);
}
