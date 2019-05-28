% rebase('base.tpl')
%import model
  <table>

    <tr>
        <td>
        <h3> ID je {{id_igre}} </h3>
        </td>
    </tr>

    <tr>
        <td>
        {{ igra.pravilni_del_gesla() }}
        </td>
    </tr>
    
    <tr>
        <td>
        {{ igra.nepravilni_ugibi() }}
        </td>
    </tr>  

    % if poskus == model.ZMAGA or poskus == model.PORAZ: 
    <form action="/nova_igra/" method="post">
        <button type="submit">Nova igra</button>
    </form>

    % else:
    <tr>
        <form action="/igra/" method="post">
        <input type="text" name="poskus">
        <input type="submit" value="Ugibaj">
        </form>

    </tr>

    % end

  </table>