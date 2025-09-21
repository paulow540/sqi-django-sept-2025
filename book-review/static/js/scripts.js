
// CSRF helper for Django fetch
function getCookie(name) {
let cookieValue = null;
if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
    const cookie = cookies[i].trim();
    if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
    }
    }
}
return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// small function to create stars string
function stars(n){
return '★'.repeat(n) + '☆'.repeat(Math.max(0,5-n));
}

// Generic client-side validation for review forms
function validateReviewForm(form){
const name = form.querySelector('[name="reviewer_name"]');
const rating = form.querySelector('[name="rating"]');
const comment = form.querySelector('[name="comment"]');
let ok = true;
// clear previous
form.querySelectorAll('.errors').forEach(e => e.remove());

if(!name || !name.value.trim()){
    const msg = document.createElement('div'); msg.className='errors'; msg.textContent='Please enter your name';
    name && name.parentNode.appendChild(msg); ok=false;
}
const r = parseInt(rating && rating.value);
if(!r || r < 1 || r > 5){
    const msg = document.createElement('div'); msg.className='errors'; msg.textContent='Rating must be 1–5';
    rating && rating.parentNode.appendChild(msg); ok=false;
}
if(!comment || comment.value.trim().length < 5){
    const msg = document.createElement('div'); msg.className='errors'; msg.textContent='Write at least 5 characters';
    comment && comment.parentNode.appendChild(msg); ok=false;
}
return ok;
}

// Example of attaching AJAX submit behaviour to review forms.
document.addEventListener('submit', async (e) => {
const form = e.target;
if(form.matches('.ajax-review-form')){
    e.preventDefault();
    if(!validateReviewForm(form)) return;

    const url = form.action || window.location.href;
    const data = new FormData(form);

    try{
    const resp = await fetch(url, {
        method: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        body: data
    });
    if(!resp.ok) throw new Error('Network error');

    const json = await resp.json().catch(()=>null);
    // If server returns the created review, append it to the reviews list
    if(json && json.success && json.review_html){
        const reviewsEl = document.querySelector('#reviews-list');
        if(reviewsEl){
        const div = document.createElement('div');
        div.innerHTML = json.review_html;
        reviewsEl.prepend(div);
        }
        // clear form
        form.reset();
    } else {
        // fallback: reload to show server-side changes
        window.location.reload();
    }
    }catch(err){
    console.error(err);
    alert('There was a problem submitting your review. Please try again.');
    }
}
});

// Small utility: decorate rating display with stars on load
document.addEventListener('DOMContentLoaded', () => {
document.querySelectorAll('[data-stars]').forEach(el=>{
    const v = parseInt(el.getAttribute('data-stars')) || 0;
    el.textContent = stars(v);
    el.classList.add('stars');
});
});

