const express = require("express");
const app     = express();
const path    = require("path");

const words = [];


app.get('/',function(req,res){
    res.sendFile(path.resolve('./index.html'));
});

app.get('/api',function(req,res){
    switch (req.query.task) {
        case 'add': {
            !words.includes(req.query.word) && words.push(req.query.word);
            //console.log(words);
            break;
        }
        case 'get': {
            res.send(JSON.stringify({words: getWords(req.query['word'])}))
        }
    }
    res.end();
});

app.listen(3200);
console.log('Started at localhost:3200');

function getWords(word) {
    return words.filter(w=>{
        return w.indexOf(word) !== -1;
    });
}