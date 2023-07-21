import {
  getAllProducts,
  getProduct,
  searchProduct,
  insertProduct,
  updateProduct,
  deleteProduct,
} from "../models/products.js";

export const _deleteProduct = (req, res) => {
  deleteProduct(req.params.id)
    .then((data) => {
      res.json(data);
    })
    .catch((e) => {
      console.log(e);
      res.status(404).json({ msg: e.message });
    });
};

export const _updateProduct = (req, res) => {
  updateProduct(req.body, req.params.id)
    .then((data) => {
      res.json(data);
    })
    .catch((e) => {
      console.log(e);
      res.status(404).json({ msg: e.message });
    });
};

export const _insertProduct = (req, res) => {
  // console.log("body", req.body);
  insertProduct(req.body)
    .then((data) => {
      // res.json(data);
      _getAllProducts(req,res)
    })
    .catch((e) => {
      console.log(e);
      res.status(404).json({ msg: e.message });
    });
};

export const _getProduct = (req, res) => {
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
export const _getAllProducts = (req, res) => {
  getAllProducts()
    .then((data) => {
      res.json(data);
    })
    .catch((e) => {
      console.log(e);
      res.status(404).json({ msg: e.message });
    });
};

export const _searchProduct = (req, res) => {
  searchProduct(req.query.name)
    .then((data) => {
      res.json(data);
    })
    .catch((e) => {
      console.log(e);
      res.status(404).json({ msg: e.message });
    });
};

export const _getAllProductsEjs = (req, res) => {
  getAllProducts()
    .then((data) => {
      res.render('shop', {
         data 
      });
    })
    .catch((e) => {
      res.render('404');
    });
};




