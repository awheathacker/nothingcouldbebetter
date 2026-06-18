import React, { useState } from 'react';
import { useForumPosts, createPost } from '../api';

function CreatePostForm() {
  return (
    <div className="create-profile-form">
      <h3 style={{ color: 'var(--text-secondary)', marginBottom: 16 }}>
        Share Your Musing
      </h3>
      <p style={{ color: 'var(--text-dim)', marginBottom: 16 }}>
        Add a post to the void board.
      </p>
      <CreatePostInner />
    </div>
  );
}

function CreatePostInner() {
  const [form, setForm] = useState({
    author: '',
    title: '',
    content: '',
    tags: '',
  });
  const [status, setStatus] = useState('idle');
  const { refresh } = useForumPosts();

  const updateField = (field) => (e) => {
    setForm(prev => ({ ...prev, [field]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus('submitting');
    try {
      const postData = {
        author: form.author,
        title: form.title,
        content: form.content,
        tags: form.tags.split(',').map(t => t.trim()).filter(Boolean),
      };
      await createPost(postData);
      setStatus('success');
      refresh();
      setForm({ author: '', title: '', content: '', tags: '' });
    } catch (err) {
      setStatus('error');
      console.error('Post creation failed:', err);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-group">
        <label for="author">Username</label>
        <input
          id="author"
          type="text"
          value={form.author}
          onChange={updateField('author')}
          placeholder="your_void_walker"
          required
        />
      </div>

      <div className="form-group">
        <label for="title">Title</label>
        <input
          id="title"
          type="text"
          value={form.title}
          onChange={updateField('title')}
          placeholder="The meaning of nothing"
          required
        />
      </div>

      <div className="form-group">
        <label for="content">Content</label>
        <textarea
          id="content"
          value={form.content}
          onChange={updateField('content')}
          placeholder="I was thinking about how..."
          required
        />
      </div>

      <div className="form-group">
        <label for="tags">Tags (comma-separated)</label>
        <input
          id="tags"
          type="text"
          value={form.tags}
          onChange={updateField('tags')}
          placeholder="existentialism, void, entropy"
        />
      </div>

      <button
        type="submit"
        className="form-submit-btn"
        disabled={status === 'submitting'}
      >
        {status === 'submitting' ? 'Posting to the void...' : 'Post'}
      </button>

      {status === 'error' && (
        <p style={{ color: 'var(--warning)', marginTop: 12 }}>
          The void rejected your musing.
        </p>
      )}
    </form>
  );
}

export default CreatePostForm;
