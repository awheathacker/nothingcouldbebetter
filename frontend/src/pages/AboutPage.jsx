import React from 'react';

function AboutPage() {
  return (
    <div className="main-content">
      <section className="section">
        <h2 className="section-title">About Nothing</h2>
        <div style={{ color: 'var(--text-muted)', lineHeight: 1.8 }}>
          <p style={{ marginBottom: 16 }}>
            <strong style={{ color: 'var(--text-secondary)'}}>Nothing Could Be Better</strong> is a gathering 
            place for people who believe life has no objective meaning, purpose, or intrinsic value.
          </p>
          <p style={{ marginBottom: 16 }}>
            We don't make money on this site. We don't want to change the world. We just want to find 
            someone who gets it.
          </p>
          <p style={{ marginBottom: 16 }}>
            Everything matters so little that we might as well enjoy it.
          </p>
          <div style={{
            background: 'var(--bg-card)',
            border: '1px solid var(--border)',
            borderRadius: 12,
            padding: 24,
            marginTop: 24,
          }}>
            <h3 style={{ color: 'var(--text-secondary)', marginBottom: 12 }}>How It Works</h3>
            <ul style={{ paddingLeft: 24, listStyle: 'disc' }}>
              <li style={{ marginBottom: 8 }}>Create a profile — share your dread level and favorite nothing</li>
              <li style={{ marginBottom: 8 }}>Find matches — our algorithm finds your void twin</li>
              <li style={{ marginBottom: 8 }}>Join the forum — share existential musings</li>
              <li style={{ marginBottom: 8 }}>Enjoy the meaninglessness</li>
            </ul>
          </div>
          <div style={{
            background: 'var(--bg-card)',
            border: '1px solid var(--border)',
            borderRadius: 12,
            padding: 24,
            marginTop: 24,
          }}>
            <h3 style={{ color: 'var(--text-secondary)', marginBottom: 12 }}>Frequently Asked Questions</h3>
            <p style={{ marginBottom: 8 }}><strong style={{ color: 'var(--text-muted)'}}>Q: Is there really nothing to do here?</strong></p>
            <p style={{ marginBottom: 16 }}>A: Nothing. Which is the point.</p>
            <p style={{ marginBottom: 8 }}><strong style={{ color: 'var(--text-muted)'}}>Q: Does any of this matter?</strong></p>
            <p style={{ marginBottom: 16 }}>A: No.</p>
            <p style={{ marginBottom: 8 }}><strong style={{ color: 'var(--text-muted)'}}>Q: Will it last?</strong></p>
            <p>A: Nothing lasts. That's part of the charm.</p>
          </div>
        </div>
      </section>
    </div>
  );
}

export default AboutPage;
