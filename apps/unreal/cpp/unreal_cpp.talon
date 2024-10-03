code.language: c
-

state you property:
  insert("UPROPERTY(BlueprintReadWrite, EditAnywhere)")

state read only you property:
    insert("UPROPERTY(BlueprintReadOnly, VisibleAnywhere)")

state you function <user.ufunction_specifiers>:
    user.insert_between("UFUNCTION({ufunction_specifiers}", ")")