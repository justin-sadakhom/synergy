import React from 'react'

function Navbar() {
    const navbar = {
        backgroundColor: '#333',
        position: 'fixed',
        top: -100,
        width: '100%',
        display: 'block',
        transition: 'top 0.3s'
    }

    const navbarA = {
        float: 'left',
        display: 'block',
        color: '#f2f2f2',
        textAlign: 'center',
        padding: '15px',
        textDecoration: 'none',
        fontSize: '17px'
    }

    window.onscroll = function() {scrollFunction()};

    return (
        <div>
            <div id = 'navbar' style = {navbar}>
                <p style ={navbarA}>Home</p>
                <p style ={navbarA}>About</p>
                <p style ={navbarA}>Contact</p>
            </div>
        </div>
    )
}

function scrollFunction() {
    if (getScrollTop() > 50) {
        document.getElementById('navbar').style.top = "0px";
    }else {
        document.getElementById('navbar').style.top = "-100px";
    }
}

function getScrollTop(){
    return window.pageYOffset ||  //most browsers
    (document.documentElement &&
       document.documentElement.scrollTop) || //
    document.body.scrollTop;
}

export default Navbar