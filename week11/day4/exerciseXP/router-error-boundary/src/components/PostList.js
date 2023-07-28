import React from 'react';
import data2 from '../data2.json'; 

const PostList = () => {
  return (
    <div>
      <h2>Post List:</h2>
      {data2.map((post) => (
        <div key={post.id}>
          <h3>{post.title}</h3>
          <p>{post.content}</p>
        </div>
      ))}
    </div>
  );
};

export default PostList;