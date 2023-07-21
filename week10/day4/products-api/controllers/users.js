import {
    register,
    login,
    updateLastLoginDate
} from "../models/users.js";
import bcrypt from 'bcrypt'

export const _register = async (req, res) => {
    try {
      const { first_name, last_name, email, username, password } = req.body;
      console.log(req.body);
      
      if (!password) {
        throw new Error("Password is required");
      }
      
      const hashedPass = await bcrypt.hash(password, 10);
      
      const row = await register( first_name, last_name, email.toLowerCase(), username, hashedPass);
      res.send(`Your username is ${req.body.username} and your password is ${req.body.password}!`);
    } catch (err) {
      res.status(500).json({ msg: err.message });
    }
  };

  export const _login = async (req, res) => {
    try {
      const { username, password } = req.body;
      const row = await login(username.toLowerCase());
      console.log(row);
      
      if (row.length === 0) {
        return res.status(404).json({ msg: "Username not found" });
      }
      
      const match = await bcrypt.compare(password, row[0].password);
      
      if (!match) {
        return res.status(400).json({ msg: "Wrong password" });
      }
      
          // Update the last_login_date to the current timestamp
    await updateLastLoginDate(username);

    res.send(`Ok Hello! your username is ${username}`);
    } catch (err) {
      res.status(500).json({ msg: err.message });
    }
  };

  // const updateLastLoginDate = async (username) => {
  //   try {
  //     const currentTimestamp = new Date().toISOString();
  //     await db('register')
  //       .where({username})
  //       .update({ last_login_date: currentTimestamp });
  //   } catch (err) {
  //     throw new Error("Failed to update last_login_date");
  //   }
  // };
  
  
  
  
  
  
  
  
  
  