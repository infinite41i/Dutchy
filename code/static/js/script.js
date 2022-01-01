$(document).ready(function () {

    var groups = [];
    var Description = $("#buy-description").val();
    var cost = 0, kala = "";
    $(".btn-edit-list").hide();
    $(".btn-cancell").hide();
    if ($(".table-scroll").height() > 200) {
        $(".table-scroll").addClass("div-scroll");
    }
    if ($(".ul-scroll").height() > 200) {
        $(".ul-scroll").addClass("div-scroll");
    }
    $(document).on("click", "#btn-add-to-list", function () {

        kala = $("#kala").val();
        cost = $("#cost").val();
        var userId = [];
        $("input[type=checkbox]:checked").each(function () {
            userId.push($(this).val());
        });
        groups.push({kala: kala, cost: cost, userId: userId});
        ResetForm();
        FillTable(groups);
        SumCost();
    });
    $(".btn-show-box").on('click', () => {
        $("#buy-box").show(700);
        $("#btn-show").hide();
        FillTable(groups);
        SumCost();
    });
    $(".btn-hide").on('click', () => {
        groups = [];
        ResetForm();
        $("#buy-box").hide(700);
        $("#btn-show").show();
    });
    $(document).on("click", "#edit-buy-btn", function () {

        var index = $(this).attr("index");
        var item = groups[index];
        $("#kala").val(item.kala);
        $("#cost").val(item.cost);
        $("#add-toloist-form input:checkbox").each(function (index, val) {
            console.log(val, 33333333333);
            if ((item.userId.find(p => p == val.value))) {

                $(val).prop("checked", true);
            } else {

                $(val).prop("checked", false);
            }
        });
        $(".btn-edit-list").attr("index", index);
        $(".btn-edit-list").show();
        $(".btn-cancell").show();
        $(".btn-add-to-list").hide();
    });
    $(document).on("click", "#btn-edit-list", function () {
        var index = $(this).attr("index");
        var usersId = [];
        $("input[type=checkbox]:checked").each(function () {
            usersId.push($(this).val());
        });
        var group = {
            kala: $("#kala").val(),
            cost: $("#cost").val(),
            userId: usersId
        };
        groups.splice(index, 1, group);
        console.log(groups, 555555555);
        ResetForm();
        FillTable(groups);
        SumCost();
    });
    $(document).on('click', "#btn-cancell", function () {
        ResetForm();
        $(".btn-edit-list").hide();
        $(".btn-cancell").hide();
        $(".btn-add-to-list").show();
    });
    $(document).on("click", "#delete-buy-btn", function () {

        var index = parseInt($(this).attr("index"));

        groups.splice(index, 1);

        FillTable(groups);
        SumCost();


    });

    $(document).on("click", "#finish", function () {
        $("#factor").val(JSON.stringify(groups))
        console.log($("#factor").val())
        $("#factor-form").submit();
    });
});

function FillTable(data) {

    $("#table-row").html(' ');
    $(data).each(function (index, item) {
        content = `
    <tr>
       <td>${item.kala}</td>
       <td class="cost">${item.cost}</td>
       <td>${item.userId}</td>
       <td>
           <i class="icon-pencil text-warning" id="edit-buy-btn" index=${index} ></i>
           <i class="icon-trash text-danger" id="delete-buy-btn" index=${index} ></i>
       </td>
    </tr>`;

        $("#table-row").append(content);
    });
}

function SumCost() {
    var costs = 0;
    $(".cost ").each(function () {
        costs += parseInt($(this).text()) || 0;
    });
    $(".alert-info span").text(costs);
}

function ResetForm() {
    $("#kala").val(" ");
    $("#cost").val(0);
    $("input[type=checkbox]").each(function () {
        $(this).prop("checked", false)
    });
}

function CreateNewGroups() {
    $('#createModal').modal();
}

function ChrgeWallet() {
    $('#ChargeModal').modal();
}

function EditUser() {
    $('#EditUserModal').modal();
}

function JoinGroup() {
    $('#joinModal').modal();
}

function ShowBuyBox() {

}