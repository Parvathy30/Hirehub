document.addEventListener("DOMContentLoaded", function () {
    const roleField = document.querySelector("#id_role");

    const seekerSection = document.querySelector("fieldset.module:nth-of-type(2)");
    const providerSection = document.querySelector("fieldset.module:nth-of-type(3)");
    const mentorSection = document.querySelector("fieldset.module:nth-of-type(4)");

    function toggleSections() {
        const role = roleField.value;

        seekerSection.style.display = "none";
        providerSection.style.display = "none";
        mentorSection.style.display = "none";

        if (role === "seeker") {
            seekerSection.style.display = "block";
        } else if (role === "provider") {
            providerSection.style.display = "block";
        } else if (role === "mentor") {
            mentorSection.style.display = "block";
        }
    }

    roleField.addEventListener("change", toggleSections);
    toggleSections();
});
