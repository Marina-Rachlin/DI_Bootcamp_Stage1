import { db } from "../config/db.js";

export const getAllProducts = () => {
  return db("products").select("id", "name", "price").orderBy("name");
};

export const getProduct = (id) => {
  return db("products").select("id", "name", "price").where({ id });//
};


//In this context, { id } is equivalent to { id: id }. It creates an object with a property named id and assigns the value of the id parameter to it.

// name = ip
export const searchProduct = (name) => {
  return db("products")
    .select("id", "name", "price")
    .whereILike("name", `${name}%`);
};

// {"name":"iBlaBla", "price": 88 }
export const insertProduct = ({name, price}) => {
  // console.log('name',name, 'price', price);
  return db('products')
  .insert ({name, price})
  .returning(['id','name','price'])
}


export const updateProduct = ({name,price}, id) => {
  return db('products')
  .update({name, price})
  .where({id})
  .returning(['id','name','price'])
}

export const deleteProduct = (id) => {
  return db('products')
  .where({id})
  .del()
  .returning(['id','name','price'])
}
