const express = require("express");
const { products } = require("./config/data.js");

const app = express();
app.use(express.urlencoded({extended:true}));
app.use(express.json());

app.listen(3001, () => {
  console.log(`server is listneing on port 3001`);
});

// CRUD - Create - Read - Update - Delete
// Create - POST
// Read - GET
// Update - PUT
// Delete - DELETE

app.get("/api/products", (req, res) => {
  res.json(products);
});

// GET - get one product with id
app.get("/api/products/:product_id", (req, res) => {
  console.log(req.params);
  const productid = req.params.product_id;

  const product = products.find((item) => item.id == productid);
  if (!product) return res.status(404).json({ msg: "Product not found" });
  res.json(product);
});

// Read - GET searche a product with query ?name=ip
app.get("/api/search", (req, res) => {
  console.log(req.query);
  const name = req.query.name;
  const filtered = products.filter((item) => {
    return item.name.toLowerCase().includes(name.toLowerCase());
  });
  if(filtered.length === 0) {
    return res.status(404).json({msg:'No product matched your search!!!'})
  }
  res.json(filtered);
});


//ADD NEW PRODUCT
app.post('/api/products', (req, res) => {
    products.push(req.body);
    res.status(201).json(products)
})

app.put('/api/products/:id/update', (req, res) => {
    const id = req.params.id; // Retrieve the ID from the URL parameter
    const updatedProduct = req.body; // Assuming the updated product data is sent in the request body
  
     // Find the index of the product in the array based on its ID
    const productIndex = products.findIndex((item) => item.id === id);

  // If the product is found, update its properties
    if (productIndex !== -1) {
     products[productIndex] = {
      ...products[productIndex],
      ...updatedProduct,
    };
}
  
    // Example response indicating the product has been updated
    res.json({ message: `Product with ID ${id} has been updated`, updatedProduct });
  });
  





