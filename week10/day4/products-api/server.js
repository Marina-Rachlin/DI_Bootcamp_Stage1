import express from "express";
import dotenv from "dotenv";
import prouter from "./routes/products.js";
import router from "./routes/users.js";
import path from 'path'

const app = express();
dotenv.config();

const __dirname = path.resolve()

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use("/", express.static(__dirname + "/products-api/public"));

app.use("/api/products", prouter);
app.use("/api/users", router);


app.set('view engine', 'ejs');
app.set('views', path.join(__dirname + "/products-api", 'views'));

app.listen(process.env.PORT, () => {
  console.log(`run on port ${process.env.PORT}`);
});


// app.get('/shop', (req, res) =>{
//   res.render('shop');
// })





