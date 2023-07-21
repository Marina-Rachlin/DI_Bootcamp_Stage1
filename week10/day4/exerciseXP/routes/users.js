import express from "express";
import { _register, _login} from "../controllers/users.js";

const u_router = express.Router();

u_router.post("/register", _register);
u_router.post('/login', _login);

export default u_router;
