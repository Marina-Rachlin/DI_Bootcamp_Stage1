function isAnagram(str1, str2) {
    
    // Remove whitespace and convert strings to lowercase
    str1 = str1.replace(/\s/g, "").toLowerCase();
    str2 = str2.replace(/\s/g, "").toLowerCase();
    
    if (str1.length !== str2.length) {
      return false;
    }

    return str1.split('').sort().join('') === str2.split('').sort().join('');
  }

console.log(isAnagram("Astronomer", "Moon starer"));