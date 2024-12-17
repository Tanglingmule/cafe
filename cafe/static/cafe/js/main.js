// Add smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add fade-in effect to messages
document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelector('.messages');
    if (messages) {
        messages.style.opacity = '0';
        messages.style.transition = 'opacity 0.5s ease-in';
        setTimeout(() => {
            messages.style.opacity = '1';
        }, 100);
        
        // Auto-hide messages after 5 seconds
        setTimeout(() => {
            messages.style.opacity = '0';
            setTimeout(() => {
                messages.style.display = 'none';
            }, 500);
        }, 5000);
    }
});

// Add hover effect to nav items
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('mouseover', function() {
        this.style.transform = 'translateY(-2px)';
    });
    link.addEventListener('mouseout', function() {
        this.style.transform = 'translateY(0)';
    });
});
