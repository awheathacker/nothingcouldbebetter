import React, { useState } from 'react';
import { createProfile } from '../api';

const DREAD_LEVELS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

function CreateProfileForm({ onSuccess }) {
  const [form, setForm] = useState({
    username: '',
    dread_level: 5,
    favorite_nothing: '',
    bio: '',
    quote: 'We are all here on earth to do nothing.',
  });
  const [status, setStatus] = useState('idle');

  const updateField = (field) => (e) => {
    setForm(prev => ({ ...prev, [field]: e.target.value }));
  };

  const updateIntField = (field) => (e) => {
    setForm(prev => ({ ...prev, [field]: parseInt(e.target.value, 10) }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus('submitting');
    try {
      const result = await createProfile(form);
      setStatus('success');
      if (onSuccess) {
        onSuccess(result);
      }
      setForm({
        username: '',
        dread_level: 5,
        favorite_nothing: '',
        bio: '',
        quote: 'We are all here on earth to do nothing.',
      });
    } catch (err) {
      setStatus('error');
      console.error('Profile creation failed:', err);
    }
  };

  return (
    <form className="create-profile-form" onSubmit={handleSubmit}>
      <h3 style={{ color: 'var(--text-secondary)', marginBottom: 16 }}>
        Enter the Void (Create Profile)
      </h3>

      <div className="form-group">
        <label for="username">Username</label>
        <input
          id="username"
          type="text"
          value={form.username}
          onChange={updateField('username')}
          placeholder="@voidwalker"
          required
        />
      </div>

      <div className="form-group">
        <label for="dread_level">Dread Level (1-10)</label>
        <select
          id="dread_level"
          value={form.dread_level}
          onChange={updateIntField('dread_level')}
        >
          {DREAD_LEVELS.map(n => (
            <option key={n} value={n}>{n} — {
              n <= 3 ? 'Mild' :
              n <= 6 ? 'Moderate' :
              n <= 9 ? 'Severe' : 'Transcendent'
            }
            </option>
          ))}
        </select>
      </div>

      <div className="form-group">
        <label for="favorite_nothing">Favorite Nothing</label>
        <input
          id="favorite_nothing"
          type="text"
          value={form.favorite_nothing}
          onChange={updateField('favorite_nothing')}
          placeholder="The silence between stars"
          required
        />
      </div>

      <div className="form-group">
        <label for="bio">Bio</label>
        <textarea
          id="bio"
          value={form.bio}
          onChange={updateField('bio')}
          placeholder="I spend a lot of time considering how brief our existence is..."
          required
        />
      </div>

      <div className="form-group">
        <label for="quote">Philosophical Quote</label>
        <input
          id="quote"
          type="text"
          value={form.quote}
          onChange={updateField('quote')}
          placeholder="We are all here on earth to do nothing."
        />
      </div>

      <button
        type="submit"
        className="form-submit-btn"
        disabled={status === 'submitting'}
      >
        {status === 'submitting' ? 'Materializing...' : 'Create Profile'}
      </button>

      {status === 'error' && (
        <p style={{ color: 'var(--warning)', marginTop: 12 }}>
          Creation failed. The void was uncooperative.
        </p>
      )}
    </form>
  );
}

export default CreateProfileForm;
