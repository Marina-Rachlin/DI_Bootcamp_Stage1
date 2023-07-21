import Parser from 'rss-parser';

//Get all posts
export const _home = async (req, res) => {
  try {
    const data = await rss();
    res.render('pages/index', { posts: data });
  } catch (err) {
    console.log(err);
  }
};

//Get search page
export const _search = async (req,res) =>{
  try{
    const data = await rss();
    res.render('pages/search', {
      posts: [],
      catg: data
    });
  } catch(err) {
      console.log(err);
  } 
}

//Search by title
export const _searchTitle = async (req, res) => {
  try{
    const data = await searchTitle(req.body.title);
    res.render('pages/search', {
      posts: data.filteredPosts,
      catg: data.posts
    });
  } catch(err) {
    console.log(err);
  }
}

//Search by category
export const _searchCategory = async (req, res) => {
  try{
    const data = await searchCategory(req.body.category);
    res.render('pages/search', {
      posts: data.filteredPosts,
      catg: data.posts
    });
  } catch(err) {
    console.log(err);
  }
}

//Fetching rss data
const rss = async () => {
  const parser = new Parser();
  const feed = await parser.parseURL('https://thefactfile.org/feed/');
  return feed.items;
};

const searchCategory = async (val) => {
  let posts = await rss();
  let filteredPosts = posts.filter( post => {
    return post.categories.includes(val)
  })
  return {filteredPosts,posts};
};

const searchTitle = async (val) => {
  let posts = await rss();
  let filteredPosts = posts.filter( post => {
    return post.title.toLowerCase().includes(val.toLowerCase())
  })
  return {filteredPosts,posts};
};




