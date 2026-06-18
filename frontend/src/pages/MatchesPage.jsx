import React, { useState } from 'react';
import { useProfiles, searchMatches } from '../api';
import MatchCard from '../components/MatchCard';

function MatchesPage() {
  const { profiles } = useProfiles();
  const [selectedUser, setSelectedUser] = useState('');
  const [matches, setMatches] = useState([]);
  const [searching, setSearching] = useState(false);
  const [searched, setSearched] = useState(false);

  const handleSearch = async () => {
    if (!selectedUser) return;
    setSearching(true);
    setSearched(true);
    try {
      const results = await searchMatches(selectedUser);
      setMatches(results);
    } catch (err) {
      console.error('Match search failed:', err);
      setMatches([]);
    }
    setSearching(false);
  };

  const handleSelect = (e) => {
    setSelectedUser(e.target.value);
    setSearched(false);
    setMatches([]);
  };

  return (
    <div className="main-content">
      <section className="section">
        <h2 className="section-title">Find Your Void Twin</h2>
        <p className="section-desc">
          Discover who shares your level of nothing. Our matching algorithm considers dread alignment,
          shared voids, and philosophical overlap.
        </p>

        <div style={{ display: 'flex', gap: 12, alignItems: 'flex-end', marginBottom: 24 }}>
          <div className="form-group" style={{ flex: 1, marginBottom: 0 }}>
            <label for="match_user">Select a user</label>
            <select
              id="match_user"
              value={selectedUser}
              onChange={handleSelect}
              style={{ width: '100%', padding: '10px 14px', background: 'var(--bg-secondary)',
                       border: '1px solid var(--border)', borderRadius: 8,
                       color: 'var(--text-primary)', fontSize: '0.95rem' }}
            >
              <option value="">— Choose someone —</option>
              {profiles.map(p => (
                <option key={p.username} value={p.username}>{p.username}</option>
              ))}
            </select>
          </div>
          <button
            className="form-submit-btn"
            onClick={handleSearch}
            disabled={searching || !selectedUser}
          >
            {searching ? 'Searching...' : 'Find Matches'}
          </button>
        </div>

        {searched && matches.length === 0 && (
          <div className="empty-state">
            <p className="empty-icon">🔮</p>
            <p>No matches found. The void is vast, and your twin is still materializing.</p>
          </div>
        )}

        {matches.length > 0 && (
          <div className="match-list">
            {matches.map((m, i) => (
              <MatchCard key={i} match={m} />
            ))}
          </div>
        )}

        {profiles.length < 2 && !searched && (
          <div className="empty-state">
            <p className="empty-icon">☁️</p>
            <p>Need more souls in the void. Add profiles first!</p>
          </div>
        )}
      </section>
    </div>
  );
}

export default MatchesPage;
