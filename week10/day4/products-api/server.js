const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const bodyParser = require('body-parser');


const app = express();
dotenv.config();

const port = process.env.PORT || 3001;


app.use(cors());
app.use(express.urlencoded({extended:true}));
app.use(express.json());


app.listen(port || 3001, () => {
    console.log('The server is running on the port', port);
})




