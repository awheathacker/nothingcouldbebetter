import React from 'react';
import { useHero, useTaglines } from '../api';

function LandingHero() {
  const { hero, loading: heroLoading } = useHero();
  const { taglines, loading: taglinesLoading } = useTaglines();

  if (heroLoading || taglinesLoading) {
    return <div className="hero"><p>Loading nothing...</p></div>;
  }

  if (!hero) return null;

  const randomTagline = taglines[Math.floor(Math.random() * taglines.length)];

  return (
    <header className="hero">
      <h1>{hero.title}</h1>
      <p className="subtitle">{hero.subtitle}</p>
      {randomTagline && (
        <p className="tagline">"{randomLineText(randomTagline)}" — {randomTagline.author}</p>
      )}
      <p className="body-text">{hero.body}</p>
      <a href="/profiles" className="cta-button">{hero.cta}</a>
    </header>
  );
}

function randomLineText(tagline) {
  return tagline.text;
}

export default LandingHero;
