"use strict";

// ================= COMMON FUNCTION =================
const elementToggleFunc = (elem) => elem.classList.toggle("active");


// ================= SIDEBAR =================
const sidebar = document.querySelector("[data-sidebar]");
const sidebarBtn = document.querySelector("[data-sidebar-btn]");

if (sidebar && sidebarBtn) {
    sidebarBtn.addEventListener("click", () => {
        elementToggleFunc(sidebar);
    });
}


// ================= TESTIMONIAL MODAL =================
const testimonialsItem = document.querySelectorAll("[data-testimonials-item]");
const modalContainer = document.querySelector("[data-modal-container]");
const modalCloseBtn = document.querySelector("[data-modal-close-btn]");
const overlay = document.querySelector("[data-overlay]");

const modalImg = document.querySelector("[data-modal-img]");
const modalTitle = document.querySelector("[data-modal-title]");
const modalText = document.querySelector("[data-modal-text]");

const testimonialsModalFunc = () => {
    modalContainer.classList.toggle("active");
    overlay.classList.toggle("active");
};

testimonialsItem.forEach(item => {
    item.addEventListener("click", () => {

        modalImg.src =
            item.querySelector("[data-testimonials-avatar]").src;

        modalImg.alt =
            item.querySelector("[data-testimonials-avatar]").alt;

        modalTitle.innerHTML =
            item.querySelector("[data-testimonials-title]").innerHTML;

        modalText.innerHTML =
            item.querySelector("[data-testimonials-text]").innerHTML;

        testimonialsModalFunc();
    });
});

if (modalCloseBtn)
    modalCloseBtn.addEventListener("click", testimonialsModalFunc);

if (overlay)
    overlay.addEventListener("click", testimonialsModalFunc);


// ================= FILTER =================
const select = document.querySelector("[data-select]");
const selectItems = document.querySelectorAll("[data-select-item]");
const selectValue = document.querySelector("[data-selecct-value]");
const filterBtn = document.querySelectorAll("[data-filter-btn]");
const filterItems = document.querySelectorAll("[data-filter-item]");

if (select) {
    select.addEventListener("click", () => {
        elementToggleFunc(select);
    });
}

function filterFunc(selectedValue) {

    filterItems.forEach(item => {

        if (
            selectedValue === "all" ||
            selectedValue === item.dataset.category
        ) {
            item.classList.add("active");
        } else {
            item.classList.remove("active");
        }

    });

}

selectItems.forEach(item => {

    item.addEventListener("click", () => {

        const value = item.innerText.toLowerCase();

        if (selectValue)
            selectValue.innerText = item.innerText;

        elementToggleFunc(select);

        filterFunc(value);

    });

});

let lastClickedBtn = filterBtn[0];

filterBtn.forEach(btn => {

    btn.addEventListener("click", () => {

        const value = btn.innerText.toLowerCase();

        if (selectValue)
            selectValue.innerText = btn.innerText;

        filterFunc(value);

        if (lastClickedBtn)
            lastClickedBtn.classList.remove("active");

        btn.classList.add("active");
        lastClickedBtn = btn;

    });

});


// ================= CONTACT FORM VALIDATION =================
const form = document.querySelector("[data-form]");
const formInputs = document.querySelectorAll("[data-form-input]");
const formBtn = document.querySelector("[data-form-btn]");

if (form) {

    formInputs.forEach(input => {

        input.addEventListener("input", () => {

            if (form.checkValidity()) {
                formBtn.removeAttribute("disabled");
            } else {
                formBtn.setAttribute("disabled", "");
            }

        });

    });

}


// ================= CONTACT FORM SUBMIT =================
const contactForm = document.getElementById("contactForm");

if (contactForm) {

    contactForm.addEventListener("submit", function (e) {

        e.preventDefault();

        fetch("/contact/", {
            method: "POST",
            body: new FormData(contactForm)
        })

        .then(res => res.json())

        .then(data => {

            const msg = document.getElementById("form-message");

            if (!msg) return;

            msg.style.display = "block";
            msg.innerHTML = data.message;

            if (data.status === "success") {

                msg.style.color = "#00ff99";
                contactForm.reset();

            } else {

                msg.style.color = "#ff4444";

            }

        })

        .catch(err => console.log(err));

    });

}


// ================= PAGE NAVIGATION =================

const navigationLinks = document.querySelectorAll("[data-nav-link]");
const pages = document.querySelectorAll("[data-page]");

navigationLinks.forEach((link) => {

    link.addEventListener("click", function () {

        const pageName = this.textContent.trim().toLowerCase();

        pages.forEach((page) => {

            if (page.dataset.page === pageName) {
                page.classList.add("active");
            } else {
                page.classList.remove("active");
            }

        });

        navigationLinks.forEach((btn) => {
            btn.classList.remove("active");
        });

        this.classList.add("active");

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });

    });

});