import React from 'react';

function dreadBadgeClass(category) {
  return `dread-badge dread-${category}`;
}

function ProfileCard({ profile }) {
  return (
    <div className="profile-card">
      <h3>{profile.username}</h3>
      <span className={dreadBadgeClass(profile.dread_category)}>
        Dread: {profile.dread_level}/10 ({profile.dread_category})
      </span>
      <p className="favorite-nothing">Favorite nothing: {profile.favorite_nothing}</p>
      <p className="bio">{profile.bio}</p>
    </div>
  );
}

export default ProfileCard;
