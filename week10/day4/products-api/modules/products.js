import { db } from "../config/db.js";

const getAllProducts = () => {
  return db("products")
  .select("id", "name", "price")
  .orderBy("name");
};

const getProduct = (id) => {
  return db('products')
  .select('id','name','price')
  .where({id})
}


const insertProduct = (product) => {
  return db ('products')
  .insert(product)
  .returning('*')
}

const deleteProduct = (id) => {
   return db ('products')
   .where ({id})
   .del()
   .returning('id', 'name')
}


module.exports = {
    getAllProducts,
    getProduct,
    insertProduct,
    deleteProduct
}