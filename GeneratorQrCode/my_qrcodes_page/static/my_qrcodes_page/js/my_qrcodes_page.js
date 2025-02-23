document.addEventListener("DOMContentLoaded", function () {
    const sortSelect = document.getElementById("sort");

    sortSelect.addEventListener("change", function () {
        const selectedSort = sortSelect.value;
        const currentUrl = new URL(window.location.href);

        if (selectedSort === "default") {
            // Удаляем параметр "sort" и возвращаем стандартный порядок
            currentUrl.searchParams.delete("sort");
        } else {
            // Устанавливаем сортировку в URL
            currentUrl.searchParams.set("sort", selectedSort);
        }

        window.location.href = currentUrl.toString();
    });
});
