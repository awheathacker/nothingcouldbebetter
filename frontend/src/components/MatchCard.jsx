import React from 'react';

function MatchCard({ match }) {
  return (
    <div className="match-card">
      <div className="match-users">
        <span className="user-name">{match.match_user}</span>
        <span className="match-arrow">⚡</span>
      </div>
      <div className="match-score">
        {(match.score * 100).toFixed(0)}%
      </div>
      <p className="match-reason">{match.reason}</p>
    </div>
  );
}

export default MatchCard;
