import React from 'react';
import { useProfiles, createProfile } from '../api';
import ProfileCard from '../components/ProfileCard';
import CreateProfileForm from '../components/CreateProfile';

function ProfilesPage() {
  const { profiles, loading, refresh } = useProfiles();

  const handleProfileCreated = () => {
    refresh();
  };

  return (
    <div className="main-content">
      <section className="section">
        <h2 className="section-title">The Void Walkers</h2>
        <p className="section-desc">
          Meet others who've accepted that nothing matters. All {profiles.length} of them.
        </p>

        {loading ? (
          <p style={{ color: 'var(--text-dim)' }}>Loading profiles from the void...</p>
        ) : (
          <div className="profile-grid">
            {profiles.length > 0 ? (
              profiles.map(p => (
                <ProfileCard key={p.username} profile={p} />
              ))
            ) : (
              <div style={{ gridColumn: '1 / -1' }}>
                <div className="empty-state">
                  <p className="empty-icon">☁️</p>
                  <p>No profiles yet. The void is empty.</p>
                  <p style={{ fontSize: '0.85rem', marginTop: 8 }}>
                    Be the first to materialize.
                  </p>
                </div>
              </div>
            )}
          </div>
        )}
      </section>

      <section className="section">
        <CreateProfileForm onSuccess={handleProfileCreated} />
      </section>
    </div>
  );
}

export default ProfilesPage;
