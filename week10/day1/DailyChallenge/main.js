const largeNumber = 356;

function getCurrentDateTime() {
    const currentDateTime = new Date();
    return currentDateTime.toString();
  }
  

module.exports = {
  largeNumber,
  getCurrentDateTime,
};