
                const data = "{{ qs_json }}";

                const rdata = JSON.parse(data.replace(/&quot;/g, '"'));
                console.log(rdata);

                const input = document.getElementById("search_here");

                const checkboxies = document.getElementsByClassName("prefectures");
                const checkboxiesArr = Array.from(checkboxies);
                let checkedboxies = [];
                let checkedPrefArr = [];

                function checkedbox(checked, value) {
                    if (checked) {
                        checkedboxies.push(value);
                    } else {
                        if (checkedboxies.includes(value)) {
                            checkedboxies.splice(checkedboxies.indexOf(value, 1));
                        }
                    }
                    console.log(checkedboxies);

                    for (let i = 0; i < checkedboxies.length; i++) {
                        checkedPrefArr = rdata.filter((query) => {
                            query["adress1"].includes(checkedboxies[i]);
                        });
                        checkedPrefArr.push(checkedPrefArr);
                        console.log(checkedboxies[i]);
                        console.log(checkedPrefArr);
                    }
                }

                checkedboxSearchArr = [];

                let inputStoreNameArr = [];

                input.addEventListener("keyup", (e) => {
                    box.innerHTML = "";
                    inputStoreNameArr = rdata.filter((query) =>
                        query["store_name"].includes(e.target.value)
                    );
                    inputStoreDescArr = rdata.filter((query) =>
                        query["about"].includes(e.target.value)
                    );

                    let inputAll = inputStoreNameArr.concat(inputStoreDescArr);

                    if (inputAll.length > 0) {
                        box.innerHTML += "";
                        inputAll.map((item) =>
                            let aTag1 = "'{% url " + '"top:detail" ' + item["store_id"] + " %}'";
                            const aTag = `<a class="content" href=${aTag1}>`;
                            box.innerHTML +=
                                aTag +
                                "<img src='/media/" +
                                item["photo1"] +
                                "'" +
                                "alt='dinner' />" +
                                `<span class="text"><h3 class="title">${item["store_name"]}</h3><div class="detail">${item["about"]}</div></span></a>`;
                        });
                        console.log(box.innerHTML);
                    } else {
                        box.innerHTML = "No Results found..";
                    }
                });
