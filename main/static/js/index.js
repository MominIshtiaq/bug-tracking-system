// document.addEventListener('DOMContentLoaded', function () {
//     const searchInput = document.getElementById('search-input');
//     const projectList = document.getElementById('project-list');

//     searchInput.addEventListener('input', function () {
//         const query = searchInput.value.trim();

//         if (query.length > 0) {
//             const xhr = new XMLHttpRequest();
//             xhr.open('GET', `/projects/search/?query=${encodeURIComponent(query)}`, true);

//             xhr.onload = function () {
//                 if (xhr.status >= 200 && xhr.status < 400) {
//                     const data = JSON.parse(xhr.responseText);
//                     projectList.innerHTML = ''; // Clear previous results

//                     if (data.results.length > 0) {
//                         data.results.forEach(function (project) {
                            // const projectElement = document.createElement('div');
                            // projectElement.className = 'col-12 col-md-6 col-lg-4 mb-4 d-flex';

                            // projectElement.innerHTML = `
                            //     <div class="card shadow-sm scaleup h-100 w-100">
                            //         <div class="card-body d-flex flex-column">
                            //             <div class="bg-primary img_icon">
                            //                 <img src="${project.image}" alt="Project image" class="img">
                            //             </div>
                            //             <h5 class="card-title mt-2">${project.name}</h5>
                            //             <p class="card-text flex-grow-1">${project.detail}</p>
                            //             <a href="${project.url}" class="btn btn-outline-primary">View Bugs</a>
                            //         </div>
                            //     </div>
                            // `;
                            // projectList.appendChild(projectElement);
//                         });
                    // } else {
                    //     projectList.innerHTML = `<p class="text-center">No projects found.</p>`;
                    // }
//                 }
//             };

//             xhr.send();
//         } else {
//             // If the search input is empty, reload all projects
//             reloadAllProjects();
//         }
//     });

//     // Function to reload the initial project list
//     function reloadAllProjects() {
//         const xhr = new XMLHttpRequest();
//         xhr.open('GET', `/projects/search/?query=`, true); // Send an empty query to fetch all projects

//         xhr.onload = function () {
//             if (xhr.status >= 200 && xhr.status < 400) {
//                 const data = JSON.parse(xhr.responseText);
//                 projectList.innerHTML = ''; // Clear previous results

//                 if (data.results.length > 0) {
//                     data.results.forEach(function (project) {
//                         const projectElement = document.createElement('div');
//                         projectElement.className = 'col-12 col-md-6 col-lg-4 mb-4 d-flex';

//                         projectElement.innerHTML = `
//                             <div class="card shadow-sm scaleup h-100 w-100">
//                                 <div class="card-body d-flex flex-column">
//                                     <div class="bg-primary img_icon">
//                                         <img src="${project.image}" alt="Project image" class="img">
//                                     </div>
//                                     <h5 class="card-title mt-2">${project.name}</h5>
//                                     <p class="card-text flex-grow-1">${project.detail}</p>
//                                     <a href="${project.url}" class="btn btn-outline-primary">View Bugs</a>
//                                 </div>
//                             </div>
//                         `;
//                         projectList.appendChild(projectElement);
//                     });
//                 }
//             }
//         };

//         xhr.send();
//     }
// });

// const query = document.getElementById('search-input').value;
// fetch(`/projects/search/?query=${encodeURIComponent(query)}`)
//     .then(response => response.json())
//     .then(data => {
//         const projectList = document.getElementById('project-list');
//         projectList.innerHTML = ''; // Clear existing projects

//         data.results.forEach(project => {
//             // Append each project to the project list
//             projectList.innerHTML += `
//                 <div class="col-12 col-md-6 col-lg-4 mb-4 d-flex">
//                     <div class="card shadow-sm scaleup h-100 w-100">
//                         <div class="card-body d-flex flex-column">
//                             <div class="bg-primary img_icon">
//                                 <img src="${project.image}" alt="Project image" class="img">
//                             </div>
//                             <h5 class="card-title mt-2">${project.name}</h5>
//                             <p class="card-text flex-grow-1">${project.detail}</p>
//                             <a href="${project.url}" class="btn btn-outline-primary">View Bugs</a>
//                         </div>
//                     </div>
//                 </div>`;
//         });
//     })
//     .catch(error => console.error('Error:', error));
