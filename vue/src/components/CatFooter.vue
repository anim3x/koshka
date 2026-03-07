<template>
    <footer>
        <a  className="git-link"
            href="https://github.com/anim3x/koshka"
            target="_blank">
        <img src='/src/assets/github-ico.png' class="git-ico" />
         </a>
        <span class="foot-info">
            koshka v1.0
        </span>
    </footer>
</template>

<style>
    footer {
        display: flex;
        align-items: center; 
        background-color: #6dbbe9;
        height: 6vh;
        margin-top: auto;
    }

    .foot-info {
        margin-left: 0.75rem;
        font-size: 1.15rem;
        color: #fff;
    }

    .git-ico {
        margin-left: 1.5rem;
        width: 1.75rem;
        height: 1.5rem;
    }
</style>