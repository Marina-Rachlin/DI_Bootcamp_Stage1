import { register, login, updateLastLogin } from "../models/users.js";
import bcrypt from "bcrypt";

export const _login = async (req, res) => {
  const { username, password } = req.body;
  try {
    // try to get password with username
    const userinfo = await login(username);

    // if username does not exist
    if (userinfo.length === 0)
      // return res.status(404).json({ msg: "username not found" });
      return res.json("Username not found!");

    // check password
    const match = bcrypt.compareSync(password + "", userinfo[0].password);

    // if password not match
    // if (!match) return res.status(401).json({ msg: "wrong password" });
    if (!match) return res.json("wrong password" );

    // update last login time
    await updateLastLogin(username);

    // response with user data without the password
    // res.status(200).json({ userinfo: { ...userinfo[0], password: "" } });
    res.json(`Welcome back ${userinfo[0].first_name} `);
  } catch (err) {
    console.log(err);
    // return res.status(404).json({ msg: "something went wrong" });
    return res.json("something went wrong");
  }
};

export const _register = async (req, res) => {
  const { fname, lname, username, email, password } = req.body;

  // encrypt the password
  const salt = bcrypt.genSaltSync(10);
  const hash = bcrypt.hashSync(password + "", salt);

  try {
    // save to db
    const rows = await register({
      first_name: fname,
      last_name: lname,
      username,
      email: email.toLowerCase(),
      hash,
    });

    // response with user info
    // res.json(rows);
    res.json(`Ok! Hello ${rows[0].first_name}. Your id is ${rows[0].user_id} `);
  } catch (err) {
    console.log(err);
    // res.status(404).json({ msg: err.message });
    res.json("Username or email already exists!");
  }
};