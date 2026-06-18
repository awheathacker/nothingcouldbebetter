import React from 'react';
import LandingHero from '../components/LandingHero';
import { useTaglines } from '../api';

function PhilosophySection() {
  const { taglines } = useTaglines();

  return (
    <section className="section">
      <h2 className="section-title">Existential Musings</h2>
      <p className="section-desc">Words from the void, attributed to thinkers who stared too long.</p>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
        {taglines.slice(0, 5).map((t, i) => (
          <div key={i} style={{
            background: 'var(--bg-card)',
            border: '1px solid var(--border)',
            borderRadius: 8,
            padding: '16px 20px',
          }}>
            <p style={{ color: 'var(--text-secondary)', fontStyle: 'italic', fontSize: '1rem' }}>
              "{t.text}"
            </p>
            <p style={{ color: 'var(--text-dim)', marginTop: 6, fontSize: '0.85rem' }}>— {t.author}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

function HomePage() {
  return (
    <div>
      <LandingHero />
      <div className="main-content">
        <PhilosophySection />
      </div>
    </div>
  );
}

export default HomePage;
