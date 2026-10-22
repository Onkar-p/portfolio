/* =============================================
   ONKAR PURJALKAR — PORTFOLIO APP LOGIC
   ============================================= */

// ─── Animated Particle Background ───────────────
const canvas = document.getElementById('bg-canvas');
const ctx = canvas.getContext('2d');

let particles = [];
const PARTICLE_COUNT = 60;

function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

class Particle {
  constructor() {
    this.reset();
  }
  reset() {
    this.x = Math.random() * canvas.width;
    this.y = Math.random() * canvas.height;
    this.size = Math.random() * 2 + 0.5;
    this.speedX = (Math.random() - 0.5) * 0.4;
    this.speedY = (Math.random() - 0.5) * 0.4;
    this.opacity = Math.random() * 0.5 + 0.1;
    const colors = ['123, 97, 255', '0, 212, 170', '255, 107, 53', '224, 64, 251'];
    this.color = colors[Math.floor(Math.random() * colors.length)];
  }
  update() {
    this.x += this.speedX;
    this.y += this.speedY;
    if (this.x < 0 || this.x > canvas.width || this.y < 0 || this.y > canvas.height) {
      this.reset();
    }
  }
  draw() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(${this.color}, ${this.opacity})`;
    ctx.fill();
  }
}

// Initialize particles
for (let i = 0; i < PARTICLE_COUNT; i++) {
  particles.push(new Particle());
}

function drawConnections() {
  for (let i = 0; i < particles.length; i++) {
    for (let j = i + 1; j < particles.length; j++) {
      const dx = particles[i].x - particles[j].x;
      const dy = particles[i].y - particles[j].y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 120) {
        ctx.beginPath();
        ctx.moveTo(particles[i].x, particles[i].y);
        ctx.lineTo(particles[j].x, particles[j].y);
        ctx.strokeStyle = `rgba(123, 97, 255, ${0.06 * (1 - dist / 120)})`;
        ctx.lineWidth = 0.5;
        ctx.stroke();
      }
    }
  }
}

function animateParticles() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  particles.forEach(p => { p.update(); p.draw(); });
  drawConnections();
  requestAnimationFrame(animateParticles);
}
animateParticles();


// ─── Typewriter Effect ───────────────────────────
const phrases = [
  
  'Data Scientist',
  'ML Engineer',
  'data analytics',
  'B.Tech Student'
];

let phraseIndex = 0;
let charIndex = 0;
let isDeleting = false;
const typeEl = document.getElementById('typewriter');

function typeEffect() {
  const current = phrases[phraseIndex];
  if (isDeleting) {
    charIndex--;
    typeEl.textContent = current.slice(0, charIndex);
  } else {
    charIndex++;
    typeEl.textContent = current.slice(0, charIndex);
  }

  let delay = isDeleting ? 60 : 110;

  if (!isDeleting && charIndex === current.length) {
    delay = 2000;
    isDeleting = true;
  } else if (isDeleting && charIndex === 0) {
    isDeleting = false;
    phraseIndex = (phraseIndex + 1) % phrases.length;
    delay = 400;
  }

  setTimeout(typeEffect, delay);
}
typeEffect();


// ─── Navbar Scroll Effect ────────────────────────
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
  updateActiveNav();
});


// ─── Active Nav Link Highlighting ───────────────
function updateActiveNav() {
  const sections = ['home', 'about', 'skills', 'experience', 'projects', 'contact'];
  const scrollPos = window.scrollY + 200;

  sections.forEach(id => {
    const el = document.getElementById(id);
    const navEl = document.getElementById(`nav-${id}`);
    if (!el || !navEl) return;

    const top = el.offsetTop;
    const bottom = top + el.offsetHeight;

    if (scrollPos >= top && scrollPos < bottom) {
      document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
      navEl.classList.add('active');
    }
  });
}


// ─── Hamburger Menu ──────────────────────────────
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('nav-links');

hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('open');
  hamburger.classList.toggle('active');
});

document.querySelectorAll('.nav-link, .nav-btn').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    hamburger.classList.remove('active');
  });
});


// ─── Scroll Reveal Animations ────────────────────
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

function addRevealClass() {
  const targets = [
    '.about-card',
    '.about-story',
    '.skill-card',
    '.project-card',
    '.contact-item',
    '.contact-form',
    '.section-header'
  ];

  targets.forEach(selector => {
    document.querySelectorAll(selector).forEach((el, i) => {
      el.classList.add('reveal');
      el.style.transitionDelay = `${i * 0.1}s`;
      revealObserver.observe(el);
    });
  });
}
addRevealClass();


// ─── Skill Bar Animation ─────────────────────────
const skillObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll('.skill-bar').forEach(bar => {
        bar.classList.add('animate');
      });
    }
  });
}, { threshold: 0.2 });

document.querySelectorAll('.skills-grid').forEach(el => skillObserver.observe(el));


// ─── Contact Form Handler ─────────────────────────
function handleSubmit(e) {
  e.preventDefault();
  const btn = document.getElementById('submit-btn');
  const successEl = document.getElementById('form-success');

  btn.innerHTML = '<span>Sending...</span><span class="btn-icon">⏳</span>';
  btn.disabled = true;

  setTimeout(() => {
    btn.innerHTML = '<span>Sent!</span><span class="btn-icon">✅</span>';
    successEl.style.display = 'block';
    document.getElementById('contact-form').reset();

    setTimeout(() => {
      btn.innerHTML = '<span>Send Message</span><span class="btn-icon">🚀</span>';
      btn.disabled = false;
      successEl.style.display = 'none';
    }, 4000);
  }, 1500);
}


// ─── Planetary Orbital Animation ────────────────
function initOrbitalSystem() {
  const container = document.getElementById('orbital-system');
  if (!container) return;

  const SIZE   = 380;           // container px
  const CENTER = SIZE / 2;      // 190
  const SPEED_MULT = 0.45;      // global speed scale

  // Collect all chips with their orbit params
  const chips = Array.from(container.querySelectorAll('.orb-chip')).map(el => ({
    el,
    radius : parseFloat(el.dataset.ring),
    speed  : parseFloat(el.dataset.speed) * SPEED_MULT,
    angle  : parseFloat(el.dataset.start) * (Math.PI / 180), // deg → rad
  }));

  // Get the half-width of each chip (set once after first layout)
  let sized = false;

  function frame() {
    chips.forEach(chip => {
      chip.angle += chip.speed * (Math.PI / 180); // deg/frame → rad

      const x = CENTER + chip.radius * Math.cos(chip.angle);
      const y = CENTER + chip.radius * Math.sin(chip.angle);

      // Translate so chip *centre* sits on the orbit path
      chip.el.style.transform = `translate(${x - CENTER}px, ${y - CENTER}px) translate(-50%, -50%)`;
      chip.el.style.left = '50%';
      chip.el.style.top  = '50%';
    });
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
}
initOrbitalSystem();


// ─── Mouse Parallax on Hero Visual ───────────────
const heroVisual = document.querySelector('.hero-visual');
const orbitalSystem = document.getElementById('orbital-system');

if (heroVisual && orbitalSystem) {
  document.addEventListener('mousemove', (e) => {
    const rect = heroVisual.getBoundingClientRect();
    const cx = rect.left + rect.width / 2;
    const cy = rect.top + rect.height / 2;
    const dx = (e.clientX - cx) / window.innerWidth;
    const dy = (e.clientY - cy) / window.innerHeight;
    // gentle whole-system parallax shift
    orbitalSystem.style.transform = `translate(${dx * 14}px, ${dy * 14}px)`;
  });
}


// ─── Smooth Nav Scroll ───────────────────────────
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const href = this.getAttribute('href');
    const target = document.querySelector(href);
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});


// ─── Card Tilt Effect ─────────────────────────────
document.querySelectorAll('.glass-card').forEach(card => {
  card.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width - 0.5;
    const y = (e.clientY - rect.top) / rect.height - 0.5;
    card.style.transform = `perspective(1000px) rotateX(${-y * 5}deg) rotateY(${x * 5}deg) translateY(-4px)`;
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = '';
  });
});


// ─── Page Load Animation ─────────────────────────
window.addEventListener('load', () => {
  document.body.style.opacity = '0';
  document.body.style.transition = 'opacity 0.5s ease';
  requestAnimationFrame(() => {
    document.body.style.opacity = '1';
  });
});

console.log(`
  ╔════════════════════════════════════╗
  ║   Onkar Purjalkar | ML Engineer   ║
  ║   B.Tech Student | AI Developer   ║
  ╚════════════════════════════════════╝
  Built with ❤️ | © 2024
`);


/* Certification cards reveal animation */

document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".certificate-card");

  if (!("IntersectionObserver" in window)) {
    cards.forEach(card => card.classList.add("certificate-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("certificate-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  cards.forEach(card => {
    card.classList.add("certificate-hidden");
    observer.observe(card);
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("certificateModal");
  const image = document.getElementById("certificateImage");
  const title = document.getElementById("certificateTitle");
  const closeButton = document.getElementById("closeCertificate");
  const fullImageLink = document.getElementById("openFullCertificate");

  if (!modal || !image || !title || !closeButton || !fullImageLink) {
    return;
  }

  document.querySelectorAll("[data-certificate]").forEach(button => {
    button.addEventListener("click", () => {
      const path = button.dataset.certificate;

      image.src = path;
      image.alt = button.dataset.title || "Certificate preview";
      title.textContent = button.dataset.title || "Certificate";
      fullImageLink.href = path;

      modal.classList.add("active");
      modal.setAttribute("aria-hidden", "false");
      closeButton.focus();
    });
  });

  function closeModal() {
    modal.classList.remove("active");
    modal.setAttribute("aria-hidden", "true");
    image.src = "";
  }

  closeButton.addEventListener("click", closeModal);

  modal.addEventListener("click", event => {
    if (event.target === modal) {
      closeModal();
    }
  });

  document.addEventListener("keydown", event => {
    if (event.key === "Escape" && modal.classList.contains("active")) {
      closeModal();
    }
  });
});