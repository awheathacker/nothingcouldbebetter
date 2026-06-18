import React from 'react';
import { useForumPosts } from '../api';
import PostCard from '../components/PostCard';
import CreatePostForm from '../components/CreatePost';

function ForumPage() {
  const { posts, loading } = useForumPosts();

  return (
    <div className="main-content">
      <section className="section">
        <h2 className="section-title">The Void Board</h2>
        <p className="section-desc">
          Share your existential musings with kindred spirits.
        </p>

        <CreatePostForm />
      </section>

      <section className="section">
        <h2 className="section-title">Musings</h2>

        {loading ? (
          <p style={{ color: 'var(--text-dim)' }}>Loading musings from the void...</p>
        ) : (
          <div className="post-list">
            {posts.length > 0 ? (
              posts.map(p => (
                <PostCard key={p.id} post={p} />
              ))
            ) : (
              <div className="empty-state">
                <p className="empty-icon">☁️</p>
                <p>No musings yet. The void awaits your contribution.</p>
              </div>
            )}
          </div>
        )}
      </section>
    </div>
  );
}

export default ForumPage;
