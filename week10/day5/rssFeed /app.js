import cors from 'cors';
import dotenv from 'dotenv';
import express from 'express';
import router from "./server/routes/posts.js";

const app = express();
dotenv.config();

app.use(express.urlencoded({ extended: true }))
app.use(express.json())
app.use(cors());

// set the view engine to ejs
app.set('view engine', 'ejs');

// Routes
app.use('/', router);


app.set('port',process.env.PORT || 3000);
app.listen(app.get('port'), ()=>{
  console.log(`Server listining to port ${app.get('port')}`);
})
