import express from "express";
import {
  _register,
  _login
} from "../controllers/users.js";

const router = express.Router();


router.get('/register', (req, res) => {
  res.render('forms');
});

router.post('/register', _register);

router.get('/login', (req, res) => {
  res.render('forms');
});

router.post('/login', _login);


export default router;