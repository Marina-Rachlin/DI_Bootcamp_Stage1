const express = require('express');
const fs = require('fs');
const knex = require('knex');

const app = express();
const port = 3000;

app.use('/', express.static(__dirname + '/static'));

app.listen(port, () => {
    console.log('The server is running on port', port)
})

const data = 'hi marina'

// fs.writeFile('info.txt', data, 'utf-8', (err) => {
//     if(err){
//         console.log(err);
//     }
// });

// fs.readFile('info.txt', 'utf-8', (err, data) => {
//     if (err){
//         console.log(err);
//     }
//     else{
//         console.log(JSON.parse(data));
//     }
// });

const db = knex({
    client: 'pg',
    connection: {
        host : 'localhost',
        port : '5432',
        user : 'postgres',
        password: 'bubaleh23',
        database: 'joblink',
    }
})

// db.select('title', 'description')
// .from('job_job')
// .then(rows => {
//     console.log(rows);
// })
// .catch(err => {
//     console.log(err);
// })

db('job_job')
.insert([
    {intership: 'yes'}
])
.select('title', 'description')
.update({description: 'js react developer'})
.returning('*')
.where({description:'js react developer'})
.then(rows => {
    console.log(rows);
})
.catch(err => {
    console.log(err);
})

