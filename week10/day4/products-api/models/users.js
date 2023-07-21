import { db } from "../config/db.js";

// export const register = (email, password) =>{
//     return db('users')
//     .insert({email, password})
//     .returning('*')
// }

export const login = (username) => {
    return db('register')
    .select('username', 'password')
    .where ({username})
}

export const register = (first_name, last_name, email, username, password) =>{
    return db('register')
    .insert({first_name, last_name, email, username, password})
    .returning('*')
}

export const updateLastLoginDate = async (username) => {
    try {
      const currentTimestamp = new Date().toISOString();
      await db('register')
        .where({username})
        .update({ last_login_date: currentTimestamp });
    } catch (err) {
      throw new Error("Failed to update last_login_date");
    }
  };