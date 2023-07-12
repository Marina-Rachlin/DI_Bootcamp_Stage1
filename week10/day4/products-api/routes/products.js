import express from "express";
import { _getAllProducts, _getProduct, _insertProduct } from "../controllers/products.js";

const prouter = express.Router();

prouter.get("/", _getAllProducts);
prouter.get("/:id", _getProduct);
prouter.post("/products", _insertProduct);



// prouter.post('/', _)
export default prouter;