// Add event listeners for the buttons
document.addEventListener('DOMContentLoaded', function () {
    const primaryButton = document.querySelector('.primary-button');
    const secondaryButton = document.querySelector('.secondary-button');
    const demoButton = document.querySelector('.demo-button');
    const tryButton = document.querySelector('.try-button');
    const watchVideoButton = document.querySelector('.watch-video');

    if (primaryButton) {
        primaryButton.addEventListener('click', function () {
            alert('Get Started button clicked!');
        });
    }

    if (secondaryButton) {
        secondaryButton.addEventListener('click', function () {
            alert('Free Demo button clicked!');
        });
    }

    if (demoButton) {
        demoButton.addEventListener('click', function () {
            alert('Demo button clicked!');
        });
    }

    if (tryButton) {
        tryButton.addEventListener('click', function () {
            alert('Try button clicked!');
        });
    }

    if (watchVideoButton) {
        watchVideoButton.addEventListener('click', function () {
            alert('Watch Candidate\'s Video button clicked!');
        });
    }

    // Adding smooth scroll effect for anchor links (if any)
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
document.addEventListener('DOMContentLoaded', function () {
    // Event listeners for hovering over company logos
    const companyLogos = document.querySelectorAll('.company-logos .logo');

    companyLogos.forEach(logo => {
        logo.addEventListener('mouseover', function () {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 6px 10px rgba(0, 0, 0, 0.2)';
        });

        logo.addEventListener('mouseout', function () {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        });
    });

    // Event listeners for hovering over stats cards
    const stats = document.querySelectorAll('.stat, .stat1');

    stats.forEach(stat => {
        stat.addEventListener('mouseover', function () {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 6px 10px rgba(0, 0, 0, 0.2)';
        });

        stat.addEventListener('mouseout', function () {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        });
    });
});
document.addEventListener('DOMContentLoaded', function () {
    // Event listeners for the skills buttons
    const skillButtons = document.querySelectorAll('.skills-buttons .btn');

    skillButtons.forEach(button => {
        button.addEventListener('click', function () {
            alert(`${this.textContent} button clicked!`);
        });
    });

    // Event listeners for hovering over container cards
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('mouseover', function () {
            this.style.transform = 'scale(1.05)';
            this.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
        });

        card.addEventListener('mouseout', function () {
            this.style.transform = 'scale(1)';
            this.style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.1)';
        });
    });

    // Event listeners for dropdown toggle buttons
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');

    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', function (event) {
            event.stopPropagation();
            const dropdownContent = this.nextElementSibling;
            if (dropdownContent.style.display === 'block') {
                dropdownContent.style.display = 'none';
            } else {
                dropdownContent.style.display = 'block';
            }
        });
    });

    // Close dropdowns if clicked outside
    document.addEventListener('click', function (event) {
        dropdownToggles.forEach(toggle => {
            const dropdownContent = toggle.nextElementSibling;
            if (dropdownContent.style.display === 'block') {
                dropdownContent.style.display = 'none';
            }
        });
    });
});
document.addEventListener('DOMContentLoaded', function () {
    // Event listeners for demo and try buttons
    const demoButton = document.querySelector('.demo-btn');
    const tryButton = document.querySelector('.try-btn');

    if (demoButton) {
        demoButton.addEventListener('click', function () {
            alert('Demo button clicked!');
        });
    }

    if (tryButton) {
        tryButton.addEventListener('click', function () {
            alert('Try button clicked!');
        });
    }

    // Event listeners for calculate ROI and get started buttons
    const calculateROIButton = document.querySelector('.calculate-roi-btn');
    const getStartedButton1 = document.querySelector('.get-started-btn1');

    if (calculateROIButton) {
        calculateROIButton.addEventListener('click', function () {
            alert('Calculate ROI button clicked!');
        });
    }

    if (getStartedButton1) {
        getStartedButton1.addEventListener('click', function () {
            alert('Get Started button clicked!');
        });
    }

    // Event listeners for hovering over statistics boxes
    const statBoxes = document.querySelectorAll('.stat-box, .stat-box1');

    statBoxes.forEach(statBox => {
        statBox.addEventListener('mouseover', function () {
            this.style.transform = 'scale(1.05)';
            this.style.boxShadow = '0 8px 16px rgba(0, 0, 0, 0.2)';
        });

        statBox.addEventListener('mouseout', function () {
            this.style.transform = 'scale(1)';
            this.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';
        });
    });
});
document.addEventListener('DOMContentLoaded', function () {
    // Event listeners for testimonial navigation buttons
    // const navButtons = document.querySelectorAll('.navigation button');
    
    // navButtons.forEach((button, index) => {
    //     button.addEventListener('click', function () {
    //         navButtons.forEach(btn => btn.classList.remove('active'));
    //         this.classList.add('active');
    //         showTestimonial(index);
    //     });
    // });

    // function showTestimonial(index) {
    //     const testimonials = document.querySelectorAll('.testimonial-card');
    //     testimonials.forEach(testimonial => testimonial.style.display = 'none');
    //     testimonials[index].style.display = 'block';
    // }

    // Initialize the first testimonial as visible
    if (navButtons.length > 0) {
        navButtons[0].classList.add('active');
        showTestimonial(0);
    }

    // Event listeners for promo buttons
    const getStartedBtn = document.querySelector('.get-started-btn');
    const bookDemoBtn = document.querySelector('.book-demo-btn');

    if (getStartedBtn) {
        getStartedBtn.addEventListener('click', function () {
            alert('Get Started button clicked!');
        });
    }

    if (bookDemoBtn) {
        bookDemoBtn.addEventListener('click', function () {
            alert('Book Demo button clicked!');
        });
    }

    // Event listeners for footer social icons
    const socialIcons = document.querySelectorAll('.social-icons img');

    socialIcons.forEach(icon => {
        icon.addEventListener('mouseover', function () {
            this.style.transform = 'scale(1.2)';
            this.style.opacity = '0.8';
        });

        icon.addEventListener('mouseout', function () {
            this.style.transform = 'scale(1)';
            this.style.opacity = '1';
        });
    });
});
