import { db } from "../config/db.js";

export const login = (username) => {
  return db("hashpwd")
    .join("users", { "users.username": "hashpwd.username" })
    .select(
      "hashpwd.password",
      "hashpwd.login_id",
      "hashpwd.username",
      "users.user_id",
      "users.first_name",
      "users.last_name",
      "users.email"
    )
    .where({ 'hashpwd.username': username });
};

export const updateLastLogin = (username) => {
  return db("users").update({ last_login: new Date() }).where({ username });
};

export const register = async ({
  first_name,
  last_name,
  username,
  email,
  hash,
}) => {
  const trx = await db.transaction();
  try {
    const user = await db("users")
      .insert(
        {
          first_name,
          last_name,
          username,
          email,
          last_login: new Date(),
        },
        ["user_id", "username", "email", "first_name", "last_name"]
      )
      .transacting(trx);

    console.log("user=>", user);

    const hashpwd = await db("hashpwd")
      .insert(
        {
          username,
          password: hash,
        },
        ["login_id", "username", "password"]
      )
      .transacting(trx);

    console.log("hashpwd=>", hashpwd);

    await trx.commit();
    return user;
  } catch (err) {
    console.log("err=>", err);
    await trx.rollback();
    throw new Error(err.message);
  }
};