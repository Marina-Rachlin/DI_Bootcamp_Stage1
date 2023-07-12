const {
    getAllProducts,
    getProduct, 
    insertProduct,
    deleteProduct
} = require(/../models/getAllProducts.js);

// GET- param

const _getProduct = (req, res) => {
    getProduct(req.params.id)
      .then((data) => {
        res.json(data);
      })
      .catch((e) => {
        console.log(e);
        res.status(404).json({ msg: e.message });
      });
  };
  
  // READ - GET - get all products
const _getAllProducts = (req, res) => {
    getAllProducts()
      .then((data) => {
        res.json(data);
      })
      .catch((e) => {
        console.log(e);
        res.status(404).json({ msg: e.message });
      });
  };

  const _insertProduct = (req, res) => {
    insertProduct(req.body)
    .then((data) => {
      res.json(data);
    })
    .catch((e) => {
      console.log(e);
      res.status(404).json({ msg: e.message });
    });
};


const _deleteProduct = (req, res) => {
  deleteProduct(req.params.id)
  .then((data) => {
    res.json(data);
  })
  .catch((e) => {
    console.log(e);
    res.status(404).json({ msg: e.message });
  });
};

module.exports = {
    _getProduct,
    _getAllProducts,
    _insertProduct
} 