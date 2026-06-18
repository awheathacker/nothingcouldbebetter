import React from 'react';

function PostCard({ post }) {
  return (
    <div className="post-card">
      <div className="post-header">
        <span className="post-title">{post.title}</span>
        <span className="post-meta">by {post.author} · {post.created_at}</span>
      </div>
      <p className="post-body">{post.content}</p>
      <div className="post-tags">
        {(post.tags || ['existentialism']).map(tag => (
          <span className="tag" key={tag}>{tag}</span>
        ))}
      </div>
    </div>
  );
}

export default PostCard;
