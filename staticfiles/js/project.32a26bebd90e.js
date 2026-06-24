/* Project specific Javascript goes here. */
/* Project specific Javascript goes here. */
document.addEventListener("DOMContentLoaded", function () {
    const counters = document.querySelectorAll(".counter");

    function animateCounter(el, end, duration) {
        let start = 0;
        let range = end - start;
        let stepTime = duration / range;
        let current = start;

        let timer = setInterval(() => {
            current++;
            el.textContent = current;
            if (current >= end) clearInterval(timer);
        }, stepTime);
    }

    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const end = parseInt(el.getAttribute("data-target"));
                animateCounter(el, end, 1500);
                obs.unobserve(el);
            }
        });
    });

    counters.forEach(counter => observer.observe(counter));
});



/* Our mission scroll effect */
document.addEventListener("scroll", function () {
    const hero = document.getElementById("hero");
    const card = document.getElementById("parallax-card");

    const rect = hero.getBoundingClientRect();

    // Only apply parallax while hero is in viewport
    if (rect.bottom > 0 && rect.top < window.innerHeight) {

        // Progress from 0 to 1 as you scroll through the hero
        const progress = rect.top / window.innerHeight;

        // Parallax amount (adjust -60 for stronger effect)
        const offset = progress * -80;

        card.style.transform = `translate(-50%, ${offset}px)`;
    }
});
