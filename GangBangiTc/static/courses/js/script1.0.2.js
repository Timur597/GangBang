let d = document
let menuButton = d.getElementById('hamburger'),
    menu = d.getElementById('menu'),
    button = d.querySelectorAll('a.closeButton')

// window.onload = () => {
//     console.log('DOM полностью загружен и разобран')
// }

window.onload = function() { 
    if (document.readyState !== "complete") {
        document.querySelector("body").style.visibility = "hidden"
        document.querySelector("#center").style.visibility = "visible" 
    } else { 
        document.querySelector("#center").style.display = "none" 
        document.querySelector("body").style.visibility = "visible"
    }
};

AOS.init({
    offset: 200,
    duration: 400,
    easing: 'ease-in-sine',
    delay: 70,
    disable: window.innerWidth < 1024
})

menuButton.addEventListener('click', () => {
    menuButton.classList.toggle('active')
    menu.classList.toggle('active')
})

$('.slider_block').slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    responsive: [
        {
            breakpoint: 700,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 500,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
            }
        }
    ]
})
.on('setPosition', function (event, slick) {
    slick.$slides.css('height', slick.$slideTrack.height() + 'px')
})

button.forEach(element => {
    element.addEventListener('click', () => {
        menuButton.classList.remove('active')
        menu.classList.remove('active')
    })
})

let acc = d.getElementsByClassName("accordion")

for (let i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("active")

        let arrow = this.childNodes[3]
        if (arrow.classList.contains('rotated')) {
            arrow.classList.remove('rotated')
        } else {
            arrow.classList.add('rotated')
        }
        
        let panel = this.nextElementSibling
        if (panel.style.display === "block") {
            panel.style.display = "none"
        } else {
            panel.style.display = "block"
        }
    })
}

particlesJS.load('particles-js', 'assets/params/particles.json', function() {
    console.log('callback - particles.js config loaded')
})

let courses = d.querySelectorAll('.courses_item')

courses.forEach(element => {
    element.addEventListener('click', () => {
        let list = element.childNodes[5]
        list.classList.toggle('open')
    })
})

let fullname = d.getElementById('name'),
    phoneNumber = d.getElementById('phoneNumber'),
    email = d.getElementById('email')

$('#python').click(() => {
    $('#python').attr( 'checked', true )
    $('#javascript').attr( 'checked', false )
    $('#java').attr( 'checked', false )
})

$('#javascript').click(() => {
    $('#python').attr( 'checked', false )
    $('#javascript').attr( 'checked', true )
    $('#java').attr( 'checked', false )
})

$('#java').click(() => {
    $('#python').attr( 'checked', false )
    $('#javascript').attr( 'checked', false )
    $('#java').attr( 'checked', true )
})

$('#submit').click(function(e) {
    e.preventDefault();
    let language = d.getElementsByName('language')
    let selectedLanguage = ''
    for (var i = 0, length = language.length; i < length; i++) {
        if (language[i].checked) {
            selectedLanguage = language[i].value
            break;
        }
    }

    let time = d.getElementsByName('time')
    let selectedTime = ''
    for (var i = 0, length = time.length; i < length; i++) {
        if (time[i].checked) {
            selectedTime = time[i].value
            break;
        }
    }

	if (fullname.value !== '' && phoneNumber.value !== '' && email.value !== '' && selectedLanguage !== '' && selectedTime !== '') {
        $.ajax({
            url:'https://api.telegram.org/bot1420679382:AAEEPYT3oDAYMT0yH_rPKBZs_lofzlERe_Q/sendMessage',
            method:'POST',
            data:{ chat_id: '-457112547', text: 
                `
                    Имя: ${fullname.value}\nТелефон: ${phoneNumber.value}\nEmail: ${email.value}\nЯзык: ${selectedLanguage}\nВремя: ${selectedTime}
                ` 
            },
            success: function(){
                alert('Ваше сообщение было отправлено!');
            }
        });
    } else {
        alert('Поля не должны быть пустыми!');
    }
});
