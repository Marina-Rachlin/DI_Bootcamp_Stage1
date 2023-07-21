import express from "express";
import dotenv from "dotenv";
import cors from "cors";
// import { db } from "./config/db.js";
// import bcrypt from 'bcrypt';
import path from "path";
import u_router from "./routes/users.js";

const app = express();
app.use(cors());

// body-parser
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

const __dirname = path.resolve();
app.use("/", express.static(__dirname + "/public"));

dotenv.config();

app.listen(process.env.PORT || 3001, () => {
  console.log(`run on ${process.env.PORT || 3001}`);
});

app.use("/users", u_router);

// try {
//   const rows = await db("users").select("*");
//   console.log(rows);
// } catch (err) {
//   console.log(err);
// }

// const salt = bcrypt.genSaltSync(10);
// const hash = bcrypt.hashSync('123456',salt)
// console.log(salt);
// console.log(hash);
