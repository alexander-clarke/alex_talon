code.language: c
-

state you property:
  insert("UPROPERTY(BlueprintReadWrite, EditAnywhere)")

state you function <user.uproperty_specifiers>:
  user.insert_between("UPROPERTY({uproperty_specifiers}", ")")

insert you property <user.uproperty_specifiers>:
  insert(", {uproperty_specifiers}")

state read only you property:
    insert("UPROPERTY(BlueprintReadOnly, VisibleAnywhere)")

state you function <user.ufunction_specifiers>:
    user.insert_between("UFUNCTION({ufunction_specifiers}", ")")
  
insert you function [specifier] <user.ufunction_specifiers>:
  insert(", {ufunction_specifiers}")