let client = "John";

const groceries = {
  fruits: ["pear", "apple", "banana"],
  vegetables: ["tomatoes", "cucumber", "salad"],
  totalPrice: "20$",
  other: {
    payed: true,
    meansOfPayment: ["cash", "creditCard"]
  }
};

const displayGroceries = () => {
  groceries.fruits.forEach(fruit => {
    console.log(fruit);
  });
};
displayGroceries ()

const cloneGroceries = () => {
  let user = client; //changing the value of the client variable doesn't affect the user variable because user is a separate copy of the initial value of client
  client = "Betty";

  let shopping = Object.assign({}, groceries); //creates a shallow copy of the groceries object. Modifying the properties of the cloned object will affect those properties in the cloned object, but it won't affect the original object. Therefore, modifying the totalPrice and payed keys in the shopping object won't affect the groceries object.

  shopping.totalPrice = "35$"; 
  shopping.other.payed = false; 

  console.log(user); 
  console.log(shopping); 
};

cloneGroceries();

