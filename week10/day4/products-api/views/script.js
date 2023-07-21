const getData = async () => {
    try {
      const res = await fetch("/api/products");
      const data = await res.json();
      console.log(data);
      render(index, data);
    } catch (err) {
      console.log(err);
    }
  };
  getData();